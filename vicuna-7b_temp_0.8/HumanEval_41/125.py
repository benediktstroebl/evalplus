

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
    def check_collision(x1, y1, v1, x2, y2, v2):
        return not ((x1 == x2) and (y1 == y2))

    def count_collisions(positions):
        count = 0
        for i in range(n // 2):
            for j in range(n // 2):
                if check_collision(positions[i * n + j], positions[i * n + j + 1], positions[i * n + j + 2],
                                   positions[i * n + j + 3], positions[i * n + j + 4]):
                    count += 1
        return count

    positions = [(i * n + j, i * n + j + 1, i * n + j + 2, i * n + j + 3, i * n + j + 4) for i in range(n)]
    return count_collisions(positions)

if __name__ == '__main__':
    n = int(input().strip())
    answer = car_race_collision(n)
    print(answer)