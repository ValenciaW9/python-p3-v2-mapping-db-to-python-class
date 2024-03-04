from __init__ import CONN, CURSOR
from department import Department

import ipdb


def reset_database():
    Department.drop_table()
    Department.create_table()

    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

    
ipdb> Department.all
{1: <Department 1: Payroll, Building A, 5th Floor>, 2: <Department 2: Human Resources, Building C, East Wing>, 3: <Department 3: Accounting, Building B, 1st Floor>}

reset_database()
ipdb.set_trace()