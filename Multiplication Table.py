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
prodList = []
def multiTable(num):
    """"
    Creates a list of multiples of a number received as input 
    """
    global prodList
    for i in range(1, 11):
        prod = num * i
        prodList.append(prod)
  
num = int(input('Enter the number whose multiplication table is to be displayed: '))
multiTable(num)
print(prodList)
print('\n')
print('The multiplication table for {0} is:' .format(num))
for index, res in enumerate(prodList, 1): # Creates multiplication table of a number using enumerate() method
    print('{0} x {1} = {2}' .format(index, num, res))
