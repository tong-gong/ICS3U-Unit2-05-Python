#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program to calculates the total cost for a given diameter pizza.

# global variable
variable_X = 25


def local_variable():
    # This shows waht happens with local variables

    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def globalobal_variable():
    # This shows waht happens with gobal variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def main():
    # This is the function shows how local and global variables work

    local_variable()
    globalobal_variable()


if __name__ == "__main__":
    main()
