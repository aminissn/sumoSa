#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2008-2025 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    runner.py
# @author  Matthias Schwamborn
# @date    2022-03-01

from __future__ import print_function
import os
import sys

if "SUMO_HOME" in os.environ:
    sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))

import traci  # noqa
import sumolib  # noqa

sumoBinary = sumolib.checkBinary('sumo')
traci.start([sumoBinary,
             "-n", "input_net2.net.xml",
             "--no-step-log",
             ] + sys.argv[1:])

vehID = "v0"
routeID = "r0"

traci.route.add(routeID, ['SC', 'CE'])
traci.vehicle.add(vehID, routeID, departSpeed="max")
traci.vehicle.setSpeedFactor(vehID, 1)
traci.vehicle.setImperfection(vehID, 0)
traci.vehicle.setSpeedMode(vehID, 0b1011111)
print("speedMode", bin(traci.vehicle.getSpeedMode(vehID)))
while traci.simulation.getMinExpectedNumber() > 0:
    print(traci.vehicle.getSpeed(vehID))
    traci.simulationStep()

traci.close()
