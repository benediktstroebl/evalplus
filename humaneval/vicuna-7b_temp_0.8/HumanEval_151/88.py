
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    # A generator is a function that returns the next value in a sequence.
    # In this case, the generator yields the sum of the squares of the
    # odd numbers in the list, and the next value is calculated inside the
    # generator.
    for n in lst:
        if n % 2 != 0 and n >= 0:
            yield n**2

lst = [1, 3, 2, 0]
print(sum(double_the_difference(lst)))

lst = [-1, -2, 0]
print(sum(double_the_difference(lst)))

lst = [9, -2]
print(sum(double_the_difference(lst)))

lst = [0]
print(sum(double_the_difference(lst)))

lst = []
print(sum(double_the_difference(lst)))
