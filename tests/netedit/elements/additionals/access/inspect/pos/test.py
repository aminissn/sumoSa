#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2009-2025 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to additional mode
netedit.additionalMode()

# select BusStop
netedit.changeElement("busStop")

# create BusStop with default parameters
netedit.leftClick(referencePosition, netedit.positions.elements.edgeCenter1)

# select Access
netedit.changeElement("access")

# Create Access
netedit.selectAdditionalChild(netedit.attrs.access.create.parent, 0)
netedit.leftClick(referencePosition, netedit.positions.elements.edge1Ped)

# go to inspect mode
netedit.inspectMode()

# inspect Access
netedit.leftClick(referencePosition, netedit.positions.elements.edge1Ped)

# Change parameter pos with a non valid value (dummy position X)
netedit.modifyAttribute(netedit.attrs.access.inspect.pos, "dummy position", True)

# Change parameter pos with a valid value (empty)
netedit.modifyAttribute(netedit.attrs.access.inspect.pos, "", True)

# Change parameter pos with a valid value (negative)
netedit.modifyAttribute(netedit.attrs.access.inspect.pos, "-1000", True)

# Change parameter pos with a valid value (greater than lane length)
netedit.modifyAttribute(netedit.attrs.access.inspect.pos, "1000", True)

# Change parameter pos with a valid value (greater than lane length)
netedit.modifyAttribute(netedit.attrs.access.inspect.pos, "random", True)

# Change parameter pos with a valid value (middle lane)
netedit.modifyAttribute(netedit.attrs.access.inspect.pos, "2.1", True)

# Check undo redo
netedit.checkUndoRedo(referencePosition)

# save netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
