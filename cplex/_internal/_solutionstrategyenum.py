# --------------------------------------------------------------------------
# Version 12.9.0
# --------------------------------------------------------------------------
# Licensed Materials - Property of IBM
# 5725-A06 5725-A29 5724-Y48 5724-Y49 5724-Y54 5724-Y55 5655-Y21
# Copyright IBM Corporation 2000, 2019. All Rights Reserved.
# 
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with
# IBM Corp.
# --------------------------------------------------------------------------
from . import _constantsenum


class SolutionStrategy(object):
    no_check = _constantsenum.CPXCALLBACKSOLUTION_NOCHECK
    check_feasible = _constantsenum.CPXCALLBACKSOLUTION_CHECKFEAS
    propagate = _constantsenum.CPXCALLBACKSOLUTION_PROPAGATE
    solve = _constantsenum.CPXCALLBACKSOLUTION_SOLVE

    def __getitem__(self, item):
        """Converts a constant to a string."""
        if item == _constantsenum.CPXCALLBACKSOLUTION_NOCHECK:
            return 'no_check'
        if item == _constantsenum.CPXCALLBACKSOLUTION_CHECKFEAS:
            return 'check_feasible'
        if item == _constantsenum.CPXCALLBACKSOLUTION_PROPAGATE:
            return 'propagate'
        if item == _constantsenum.CPXCALLBACKSOLUTION_SOLVE:
            return 'solve'
        raise KeyError(item)
