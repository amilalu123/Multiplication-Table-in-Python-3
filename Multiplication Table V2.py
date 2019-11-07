"""
Author: Bipin P. (mailto: bipinp2013@gmail.com)
http://iambipin.com

101010101    10  101010101    10  101     10    101010101
1010101010   10  1010101010   10  1010    10    1010101010
10      101  10  10      101  10  10 01   10    10      101
10      101  10  10      101  10  10  10  10    10      101
1010101010   10  1010101010   10  10   01 10    1010101010
1010101010   10  101010101    10  10    1010    101010101
10      101  10  10           10  10     010    10
10      101  10  10           10  10      10    10
1010101010   10  10           10  10      10    10
101010101    10  10           10  10      10    10  10

Multiplication Table
In mathematics, a multiplication table (sometimes, less formally, a times table) 
is a mathematical table used to define a multiplication operation for an algebraic system.

The decimal multiplication table was traditionally taught as an essential part of elementary 
arithmetic around the world, as it lays the foundation for arithmetic operations with base-ten numbers.
Many educators believe it is necessary to memorize the table up to 9 × 9.
(Source: https://en.wikipedia.org/wiki/Multiplication_table)
"""

try:
    prodList = []
    num = int(input('Enter the number whose multiplication table is to be displayed: '))
    #num = 7

    prodList = [num * i for i in range(1, 13)]
    print(prodList)
    print('\n')
    print('The multiplication table for {0} is:' .format(num))
    for index, ele in enumerate(prodList, 1): # Creates multiplication table of a number
        print('{0} x {1} = {2}' .format(index, num, ele))
        
except(ValueError):
    print('Please enter a valid integter number')