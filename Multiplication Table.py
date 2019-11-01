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
for index, res in enumerate(prodList, 1): # Creates multiplication table of a number
    print('{0} x {1} = {2}' .format(index, num, res))