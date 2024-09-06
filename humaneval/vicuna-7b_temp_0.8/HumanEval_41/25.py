

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """

    # The formula for the number of collisions is (n choose 2) / 2^n
    # where choose is the combinatorial number of ways to choose 2 elements from n elements
    # and 2^n is the total number of ways to choose 2 elements from n elements
    # since there are n choose 2 ways to choose 2 elements from n, and each pair of elements
    # must be chosen exactly once, the total number of pairs of elements is 2^n
    # therefore the total number of collisions is (n choose 2) / 2^n

    # Let's call the total number of ways to choose 2 elements from n elements as C(n,2)
    # n choose 2 = n! / (2! (n-2)!) = n \* (n-1) \* (n-2) / 6
    # 6 is the number of possible ways to permute the elements of the set {1,2,3,4,5,6}
    # 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720
    # Therefore, C(n,2) = n \* (n-1) \* (n-2) / 6

    # The number of cars is n
    n = int(input("Enter the number of cars: "))

    # The total number of ways to choose 2 elements from n is C(n,2)
    total_collisions = n * (n - 1) * (n - 2) / 6

    # The formula for the number of cars moving in each direction is n/2
    # The number of cars moving in one direction is always half the number of cars
    num_cars_left = n // 2
    num_cars_right = n // 2

    # The number of collisions is the sum of the number of cars moving in each direction
    num_collisions = num_cars_left + num_cars_right

    # Print the answer
    print(f"There will be {total_collisions} collisions
