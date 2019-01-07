# ------------------------------------------------------------------------
# File: exceptions/error_codes.py
# ------------------------------------------------------------------------
# Licensed Materials - Property of IBM
# 5725-A06 5725-A29 5724-Y48 5724-Y49 5724-Y54 5724-Y55 5655-Y21
# Copyright IBM Corporation 2008, 2016. All Rights Reserved.
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with
# IBM Corp.
# ------------------------------------------------------------------------
"""Error codes returned by the Callable Library.

This module defines symbolic names for the integer error codes returned by
the Callable Library.  The names to which the error codes are assigned are
the same names used in the Callable Library, all of which begin with
CPXERR.  The error codes are accessible as the third element of the args
attribute of the exception that is raised.  These symbolic names should be
used to test if a particular error has occurred.  For example, to test if
a read operation failed because of insufficient memory, your program
should use the statements:

try:
    c = cplex.Cplex("big_problem.mps")
except CplexSolverError as exc:
    if exc.args[2] == cplex.exceptions.error_codes.CPXERR_NO_MEMORY:
        print "insufficient memory, reading smaller problem"
        c = cplex.Cplex("smaller_problem.mps")
"""


CPXERR_ABORT_STRONGBRANCH = 1263
CPXERR_ADJ_SIGN_QUAD = 1606
CPXERR_ADJ_SIGN_SENSE = 1604
CPXERR_ADJ_SIGNS = 1602
CPXERR_ALGNOTLICENSED = 32024
CPXERR_ARC_INDEX_RANGE = 1231
CPXERR_ARRAY_BAD_SOS_TYPE = 3009
CPXERR_ARRAY_NOT_ASCENDING = 1226
CPXERR_ARRAY_TOO_LONG = 1208
CPXERR_BAD_ARGUMENT = 1003
CPXERR_BAD_BOUND_SENSE = 1622
CPXERR_BAD_BOUND_TYPE = 1457
CPXERR_BAD_CHAR = 1537
CPXERR_BAD_CTYPE = 3021
CPXERR_BAD_DECOMPOSITION = 2002
CPXERR_BAD_DIRECTION = 3012
CPXERR_BAD_EXPO_RANGE = 1435
CPXERR_BAD_EXPONENT = 1618
CPXERR_BAD_FILETYPE = 1424
CPXERR_BAD_ID = 1617
CPXERR_BAD_INDCONSTR = 1439
CPXERR_BAD_INDICATOR = 1551
CPXERR_BAD_LAZY_UCUT = 1438
CPXERR_BAD_LUB = 1229
CPXERR_BAD_METHOD = 1292
CPXERR_BAD_NUMBER = 1434
CPXERR_BAD_OBJ_SENSE = 1487
CPXERR_BAD_PARAM_NAME = 1028
CPXERR_BAD_PARAM_NUM = 1013
CPXERR_BAD_PIVOT = 1267
CPXERR_BAD_PRIORITY = 3006
CPXERR_BAD_PROB_TYPE = 1022
CPXERR_BAD_ROW_ID = 1532
CPXERR_BAD_SECTION_BOUNDS = 1473
CPXERR_BAD_SECTION_ENDATA = 1462
CPXERR_BAD_SECTION_QMATRIX = 1475
CPXERR_BAD_SENSE = 1215
CPXERR_BAD_SOS_TYPE = 1442
CPXERR_BAD_STATUS = 1253
CPXERR_BADPRODUCT = 32023
CPXERR_BAS_FILE_SHORT = 1550
CPXERR_BAS_FILE_SIZE = 1555
CPXERR_BENDERS_MASTER_SOLVE = 2001
CPXERR_CALLBACK = 1006
CPXERR_CANT_CLOSE_CHILD = 1021
CPXERR_CHILD_OF_CHILD = 1019
CPXERR_CNTRL_IN_NAME = 1236
CPXERR_COL_INDEX_RANGE = 1201
CPXERR_COL_REPEAT_PRINT = 1478
CPXERR_COL_REPEATS = 1446
CPXERR_COL_ROW_REPEATS = 1443
CPXERR_COL_UNKNOWN = 1449
CPXERR_CONFLICT_UNSTABLE = 1720
CPXERR_COUNT_OVERLAP = 1228
CPXERR_COUNT_RANGE = 1227
CPXERR_CPUBINDING_FAILURE = 3700
CPXERR_DBL_MAX = 1233
CPXERR_DECOMPRESSION = 1027
CPXERR_DETTILIM_STRONGBRANCH = 1270
CPXERR_DUP_ENTRY = 1222
CPXERR_DYNFUNC = 1815
CPXERR_DYNLOAD = 1814
CPXERR_ENCODING_CONVERSION = 1235
CPXERR_EXTRA_BV_BOUND = 1456
CPXERR_EXTRA_FR_BOUND = 1455
CPXERR_EXTRA_FX_BOUND = 1454
CPXERR_EXTRA_INTEND = 1481
CPXERR_EXTRA_INTORG = 1480
CPXERR_EXTRA_SOSEND = 1483
CPXERR_EXTRA_SOSORG = 1482
CPXERR_FAIL_OPEN_READ = 1423
CPXERR_FAIL_OPEN_WRITE = 1422
CPXERR_FILE_ENTRIES = 1553
CPXERR_FILE_FORMAT = 1563
CPXERR_FILE_IO = 1426
CPXERR_FILTER_VARIABLE_TYPE = 3414
CPXERR_ILL_DEFINED_PWL = 1213
CPXERR_ILOG_LICENSE = 32201
CPXERR_IN_INFOCALLBACK = 1804
CPXERR_INDEX_NOT_BASIC = 1251
CPXERR_INDEX_RANGE = 1200
CPXERR_INDEX_RANGE_HIGH = 1206
CPXERR_INDEX_RANGE_LOW = 1205
CPXERR_INT_TOO_BIG = 3018
CPXERR_INT_TOO_BIG_INPUT = 1463
CPXERR_INVALID_NUMBER = 1650
CPXERR_LIMITS_TOO_BIG = 1012
CPXERR_LINE_TOO_LONG = 1465
CPXERR_LO_BOUND_REPEATS = 1459
CPXERR_LOCK_CREATE = 1808
CPXERR_LP_NOT_IN_ENVIRONMENT = 1806
CPXERR_LP_PARSE = 1427
CPXERR_MASTER_SOLVE = 2005
CPXERR_MIPSEARCH_WITH_CALLBACKS = 1805
CPXERR_MISS_SOS_TYPE = 3301
CPXERR_MSG_NO_CHANNEL = 1051
CPXERR_MSG_NO_FILEPTR = 1052
CPXERR_MSG_NO_FUNCTION = 1053
CPXERR_MULTIPLE_PROBS_IN_REMOTE_ENVIRONMENT = 1816
CPXERR_NAME_CREATION = 1209
CPXERR_NAME_NOT_FOUND = 1210
CPXERR_NAME_TOO_LONG = 1464
CPXERR_NAN = 1225
CPXERR_NEED_OPT_SOLN = 1252
CPXERR_NEGATIVE_SURPLUS = 1207
CPXERR_NET_DATA = 1530
CPXERR_NET_FILE_SHORT = 1538
CPXERR_NO_BARRIER_SOLN = 1223
CPXERR_NO_BASIC_SOLN = 1261
CPXERR_NO_BASIS = 1262
CPXERR_NO_BOUND_SENSE = 1621
CPXERR_NO_BOUND_TYPE = 1460
CPXERR_NO_COLUMNS_SECTION = 1472
CPXERR_NO_CONFLICT = 1719
CPXERR_NO_DECOMPOSITION = 2000
CPXERR_NO_DUAL_SOLN = 1232
CPXERR_NO_ENDATA = 1552
CPXERR_NO_ENVIRONMENT = 1002
CPXERR_NO_FILENAME = 1421
CPXERR_NO_ID = 1616
CPXERR_NO_ID_FIRST = 1609
CPXERR_NO_INT_X = 3023
CPXERR_NO_KAPPASTATS = 1269
CPXERR_NO_LU_FACTOR = 1258
CPXERR_NO_MEMORY = 1001
CPXERR_NO_MIPSTART = 3020
CPXERR_NO_NAME_SECTION = 1441
CPXERR_NO_NAMES = 1219
CPXERR_NO_NORMS = 1264
CPXERR_NO_NUMBER = 1615
CPXERR_NO_NUMBER_BOUND = 1623
CPXERR_NO_NUMBER_FIRST = 1611
CPXERR_NO_OBJ_SENSE = 1436
CPXERR_NO_OBJECTIVE = 1476
CPXERR_NO_OP_OR_SENSE = 1608
CPXERR_NO_OPERATOR = 1607
CPXERR_NO_ORDER = 3016
CPXERR_NO_PROBLEM = 1009
CPXERR_NO_QP_OPERATOR = 1614
CPXERR_NO_QUAD_EXP = 1612
CPXERR_NO_RHS_COEFF = 1610
CPXERR_NO_RHS_IN_OBJ = 1211
CPXERR_NO_ROW_NAME = 1486
CPXERR_NO_ROW_SENSE = 1453
CPXERR_NO_ROWS_SECTION = 1471
CPXERR_NO_SENSIT = 1260
CPXERR_NO_SOLN = 1217
CPXERR_NO_SOLNPOOL = 3024
CPXERR_NO_SOS = 3015
CPXERR_NO_TREE = 3412
CPXERR_NO_VECTOR_SOLN = 1556
CPXERR_NODE_INDEX_RANGE = 1230
CPXERR_NODE_ON_DISK = 3504
CPXERR_NOT_DUAL_UNBOUNDED = 1265
CPXERR_NOT_FIXED = 1221
CPXERR_NOT_FOR_BENDERS = 2004
CPXERR_NOT_FOR_MIP = 1017
CPXERR_NOT_FOR_QCP = 1031
CPXERR_NOT_FOR_QP = 1018
CPXERR_NOT_MILPCLASS = 1024
CPXERR_NOT_MIN_COST_FLOW = 1531
CPXERR_NOT_MIP = 3003
CPXERR_NOT_MIQPCLASS = 1029
CPXERR_NOT_ONE_PROBLEM = 1023
CPXERR_NOT_QP = 5004
CPXERR_NOT_SAV_FILE = 1560
CPXERR_NOT_UNBOUNDED = 1254
CPXERR_NULL_NAME = 1224
CPXERR_NULL_POINTER = 1004
CPXERR_ORDER_BAD_DIRECTION = 3007
CPXERR_OVERFLOW = 1810
CPXERR_PARAM_INCOMPATIBLE = 1807
CPXERR_PARAM_TOO_BIG = 1015
CPXERR_PARAM_TOO_SMALL = 1014
CPXERR_PRESLV_ABORT = 1106
CPXERR_PRESLV_BAD_PARAM = 1122
CPXERR_PRESLV_BASIS_MEM = 1107
CPXERR_PRESLV_COPYORDER = 1109
CPXERR_PRESLV_COPYSOS = 1108
CPXERR_PRESLV_CRUSHFORM = 1121
CPXERR_PRESLV_DETTIME_LIM = 1124
CPXERR_PRESLV_DUAL = 1119
CPXERR_PRESLV_FAIL_BASIS = 1114
CPXERR_PRESLV_INF = 1117
CPXERR_PRESLV_INForUNBD = 1101
CPXERR_PRESLV_NO_BASIS = 1115
CPXERR_PRESLV_NO_PROB = 1103
CPXERR_PRESLV_SOLN_MIP = 1110
CPXERR_PRESLV_SOLN_QP = 1111
CPXERR_PRESLV_START_LP = 1112
CPXERR_PRESLV_TIME_LIM = 1123
CPXERR_PRESLV_UNBD = 1118
CPXERR_PRESLV_UNCRUSHFORM = 1120
CPXERR_PRIIND = 1257
CPXERR_PRM_DATA = 1660
CPXERR_PRM_HEADER = 1661
CPXERR_PROTOCOL = 1812
CPXERR_Q_DIVISOR = 1619
CPXERR_Q_DUP_ENTRY = 5011
CPXERR_Q_NOT_INDEF = 5014
CPXERR_Q_NOT_POS_DEF = 5002
CPXERR_Q_NOT_SYMMETRIC = 5012
CPXERR_QCP_SENSE = 6002
CPXERR_QCP_SENSE_FILE = 1437
CPXERR_QUAD_EXP_NOT_2 = 1613
CPXERR_QUAD_IN_ROW = 1605
CPXERR_RANGE_SECTION_ORDER = 1474
CPXERR_RESTRICTED_VERSION = 1016
CPXERR_RHS_IN_OBJ = 1603
CPXERR_RIM_REPEATS = 1447
CPXERR_RIM_ROW_REPEATS = 1444
CPXERR_RIMNZ_REPEATS = 1479
CPXERR_ROW_INDEX_RANGE = 1203
CPXERR_ROW_REPEAT_PRINT = 1477
CPXERR_ROW_REPEATS = 1445
CPXERR_ROW_UNKNOWN = 1448
CPXERR_SAV_FILE_DATA = 1561
CPXERR_SAV_FILE_VALUE = 1564
CPXERR_SAV_FILE_WRITE = 1562
CPXERR_SBASE_ILLEGAL = 1554
CPXERR_SBASE_INCOMPAT = 1255
CPXERR_SINGULAR = 1256
CPXERR_STR_PARAM_TOO_LONG = 1026
CPXERR_SUBPROB_SOLVE = 3019
CPXERR_SYNCPRIM_CREATE = 1809
CPXERR_SYSCALL = 1813
CPXERR_THREAD_FAILED = 1234
CPXERR_TILIM_CONDITION_NO = 1268
CPXERR_TILIM_STRONGBRANCH = 1266
CPXERR_TOO_MANY_COEFFS = 1433
CPXERR_TOO_MANY_COLS = 1432
CPXERR_TOO_MANY_RIMNZ = 1485
CPXERR_TOO_MANY_RIMS = 1484
CPXERR_TOO_MANY_ROWS = 1431
CPXERR_TOO_MANY_THREADS = 1020
CPXERR_TREE_MEMORY_LIMIT = 3413
CPXERR_TUNE_MIXED = 1730
CPXERR_UNIQUE_WEIGHTS = 3010
CPXERR_UNSUPPORTED_CONSTRAINT_TYPE = 1212
CPXERR_UNSUPPORTED_OPERATION = 1811
CPXERR_UP_BOUND_REPEATS = 1458
CPXERR_WORK_FILE_OPEN = 1801
CPXERR_WORK_FILE_READ = 1802
CPXERR_WORK_FILE_WRITE = 1803
CPXERR_XMLPARSE = 1425