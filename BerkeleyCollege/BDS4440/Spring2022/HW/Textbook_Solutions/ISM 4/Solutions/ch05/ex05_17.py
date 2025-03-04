# Exercise 5.17

def is_odd(x):
    print(f'is_odd({x})')
    return x % 2 != 0

def square(x):
    print(f'square({x})')
    return x ** 2

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

list(map(square, 
    filter(is_odd, numbers)))

list(filter(is_odd, 
    map(square, numbers)))

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
