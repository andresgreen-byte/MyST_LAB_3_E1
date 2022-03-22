"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 3.                                                                                     -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: diegolazareno                                                                               -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/diegolazareno/MyST_LAB_3_E1                                          -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

from http import server
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# display data on MetaTrader 5 version
print(mt5.version())


def log_in(account,password):
    authorized=mt5.login(account, password, server="FxPro-MT5")
    if authorized:
        # display trading account data 'as is'
        print(mt5.account_info())
        # display trading account data in the form of a list
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
user_connect = log_in()


