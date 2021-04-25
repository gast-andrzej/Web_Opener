'''
2021
Author: Andrzej Gast, email: gastandrzej@gmail.com

Imports

Function


'''

import requests
import Times_Insertion
import WWW_Insertion

_vart1= Times_Insertion.b
_vart2= WWW_Insertion.a


def reqr_func(_vart1, _vart2):
    """


    :param _vart1:
    :param _vart2:
    :return:
    """
    if _vart1 > 0:
        return requests.get(f'http://{_vart2}'), print('connected'), reqr_func(_vart1-1, _vart2)
    else:
        return print('done')



reqr_func(_vart1, _vart2)
