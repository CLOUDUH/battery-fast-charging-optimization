'''
Author: CLOUDUH
Date: 2022-05-30 20:55:42
LastEditors: CLOUDUH
LastEditTime: 2022-05-30 21:09:19
Description: 
'''

from policies import charging_policy
from sim_with_seed import sim

if __name__ == '__main__':
    charging_policy('data', 'all')

    lifetime = sim(3.6, 6, 5.6, seed=1)
    print('Simulated lifetime is', lifetime)
