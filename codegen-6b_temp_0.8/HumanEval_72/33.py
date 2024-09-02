
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
    pass

    def maxi_weight(l):
        max_weight = 0
        for elt in l:
            max_weight += elt
        return max_weight

    def is_balanced(l):
        top = 0
        bot = 0

        for elt in l:
            top += elt
            bot -= elt

        if top == bot:
            return True
        else:
            return False

    def will_fly(top, bot, max_weight, l):
        if top == bot:
            return False
        elif top > bot:
            if l == []:
                return False
            else:
                top = l[0]
                bot = l[-1]
                l = l[1:-1]
                return will_fly(top, bot, max_weight, l)
        elif top < bot:
            return False

    top = 0
    bot = 0
    max_weight = maxi_weight(q)
    if max_weight <= w:
        return True
    else:
        return False
