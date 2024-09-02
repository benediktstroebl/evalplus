
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    #print(list(range(int(a),int(b)+1)) )
    num_list=[]
    for i in range(int(a),int(b)+1):
        if i%2==0:
            num_list.append(i)
    #print(num_list)
    return num_list


