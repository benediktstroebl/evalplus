
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # 문제에서 요구하는 범위가 2 ~ 8 이므로 정수 100을 범위로 설정해 볼까?
    # 문제에서 요구하는 조건은 2 ~ 8 정수 범위이므로, 기본 값 범위를 넘기지 않으면서, 범위를 좁혀나갈 수 있는 범위를 정수 100으로 설정해봤으나 결과가 바람직하지 않음.
    # 즉, 처음에 정수 100을 범위로 설정하면 2 ~ 8 범위 밖의 수를 생성하는 문제가 되기 때문
    # 따라서 정수 100을 범위로 설정
