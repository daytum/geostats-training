#!/usr/bin/env python

# Copyright 2018-2020 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np
import unittest

def cleanup(line):

    return line.strip().strip('\n').split()

def get_gold_pressures():

    return np.load('test.npy')

def get_cmg_pressures():

    with open('assignment18.txt') as f:

        raw_content = f.readlines()


    pressure = []
    for i in range(len(raw_content)):
        line = raw_content[i]
        clean_line = cleanup(line) 

        if clean_line != []:
            if clean_line[1] == 'K':
                pressure += [cleanup(raw_content[i+1])]

    return np.array(pressure, dtype=np.double)


class TestSolution(unittest.TestCase):


    def test_output_pressures(self):

        np.testing.assert_allclose(get_cmg_pressures(), get_gold_pressures(),
                                   atol=1)
        return


if __name__ == '__main__':
            unittest.main()
