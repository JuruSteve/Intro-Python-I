# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(nbr):
    if (int(nbr) % 2) == 0:
        print('Even!!')
        return True
    else:
        print('Odd!!')
        return False


is_even(4)
is_even(7)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
if num % 2 == 0:
    print('Even')
else:
    print('Odd')
