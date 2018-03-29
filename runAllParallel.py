
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth
# Floor, Boston, MA 02110-1301, USA.
# 
# 
# Code:
# Figure out how to convert a given molecule to buffered for doing dose-resp
# To do: Provide a way to set model modifications
# Provide way to plot on log scale if dose-response
# Put in stuff with respect to a ratio


# Feb12 2018: Taken from Upi's labnotes autsim12.py and manipulate for the current excel sheet

'''
*******************************************************************
 * File:            runAllParallel.py
 * Description:
 * Author:          Upinder S. Bhalla
 * E-mail:          bhalla@ncbs.res.in
 ********************************************************************/

/**********************************************************************
** This program is part of 'MOOSE', the
** Messaging Object Oriented Simulation Environment,
**           copyright (C) 2003-2018 Upinder S. Bhalla. and NCBS
**********************************************************************/

This script runs the findSim program on all tsv files in the specified
directory, computes their scores, and prints out basic stats of the scores.
It can do this in parallel using Python's multiprocessing library.
'''

import numpy
import argparse
import os
import argparse
import findSim
from multiprocessing import Pool

def main():
    parser = argparse.ArgumentParser( description = 'Wrapper script to run a lot of FindSim evaluations in parallel.' )

    parser.add_argument( 'location', type = str, help='Required: Directory in which the scripts (in tsv format) are all located.')
    parser.add_argument( '--numProcesses', type = int, help='Optional: Number of processes to spawn', default = 2 )
    args = parser.parse_args()

    fnames = [ i for i in os.listdir( args.location ) if i.endswith( ".tsv" )]
    pool = Pool( processes = args.numProcesses )
    #ret = findSim.innerMain(fnames[0], hideDisplay=True)

    ret = [pool.apply_async( findSim.innerMain, (i,), dict(hideDisplay=True)) for i in fnames ]
    print( "scores = " )
    for i, j in zip( fnames, ret ):
        print i, j
        #print( "{0} : {1:.2f}".format( i, j ) )

        
# Run the 'main' if this script is executed standalone.
if __name__ == '__main__':
    main()
