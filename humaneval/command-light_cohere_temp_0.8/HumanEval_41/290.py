```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 

    two sets of cars start out being very far from each other. All cars move in the same speed. When a car that's moving left to right hits a car that's moving right to left, the cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.

    return the number of collisions.

def test_collision(n: int):
    # Test case 1: All cars drive right at the same speed
    car1 = [0 for i in range(n)]
    car2 = [0 for i in range(n)]
    car3 = [0 for i in range(n)]
    for i in range(n):
        car1[i] = 1
        car2[i] = 0
        car3[i] = 0
    car1[i] = car2[i]
    car2[i] = car3[i]
    car3[i] = 0
    # Test case 2: Two cars drive right at the same time
    car1 = [0 for i in range(n)]
    car2 = [0 for i in range(n)]
    car3 = [0 for i in range(n)]
    car4 = [0 for i in range(n)]
    car5 = [0 for i in range(n)]
    car6 = [0 for i in range(n)]
    car7 = [0 for i in range(n)]
    car8 = [0 for i in range(n)]
    car9 = [0 for i in range(n)]
    for i in range(n):
        car1[i] = 1
        car2[i] = 0
        car3[i] = 0
        car4[i] = 0
        car5[i] = 1
        car6[i] = 0
        car7[i] = 0
        car8[i] = 0
        car9[i] = 0
    car1[i] = car2[i]
    car2[i] = car3[i]
    car3[i] = car4[i]
    car4[i] = car5[i]
    car5[i] = car6[i]
    car6[i] = car7[i]
    car7[i] = car8[i]
    car8[i] = car9[i]
    car9[i] = 1
    # Test case 3: Two cars drive left at the same time
    car1 = [0 for i in range(n)]
    car2 = [0 for i in range(n)]
    car3 = [0 for i in range(n)]
    car4 = [0 for i in range(n)]
    car5 = [0 for i in range(n)]
    car6 = [0 for i in range(n)]
    car7 = [0 for i in range(n)]
    car8 = [0 for i in range(n)]
    car9 = [0 for i in range(n)]
    for i in range(n):
        car1[i] = 1
        car2[i] = 0
        car3[i] = 0
        car4[i] = 0
        car5[i] = 1
        car6[i] = 0
        car7[i] = 0
        car8[i] = 0