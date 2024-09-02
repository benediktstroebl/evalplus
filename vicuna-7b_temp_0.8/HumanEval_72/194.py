
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    return (q[0] == q[len(q)-1] and sum(q) <= w)

q = [5, 3, 10, 7, 1, 9]
for i in range(len(q)):
    print(q[i])
    print(i)
    print(will_it_fly(q, 5))
    print(will_it_fly(q, 10))
    print(will_it_fly(q, 15))
    print(will_it_fly(q, 20))
    print(will_it_fly(q, 25))
    print(will_it_fly(q, 30))
    print(will_it_fly(q, 35))
    print(will_it_fly(q, 40))
    print(will_it_fly(q, 45))
    print(will_it_fly(q, 50))
    print(will_it_fly(q, 55))
    print(will_it_fly(q, 60))
    print(will_it_fly(q, 65))
    print(will_it_fly(q, 70))
    print(will_it_fly(q, 75))
    print(will_it_fly(q, 80))
    print(will_it_fly(q, 85))
    print(will_it_fly(q, 90))
    print(will_it_fly(q, 95))
    print(will_it_fly(q, 100))
    print(will_it_fly(q, 105))
    print(will_it_fly(q, 110))
    print(will_it_fly(q, 115))
    print(will_it_fly(q, 120))
    print(will_it_fly(q, 125))
    print(will_it_fly(q, 130))
    print(will_it_fly(q, 135))
    
