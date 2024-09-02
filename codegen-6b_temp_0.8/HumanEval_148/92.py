
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter",
               "Saturn", "Uranus", "Neptune")

    def root(a, b):
        # Find the floored square root of a^2 + b^2
        x, y = abs(a), abs(b)
        while y:
            x, y = y, x % y
        return x

    def sign(a, b):
        # Return the sign of a * b
        return (a, b)[a * b < 0]

    def check(planet1, planet2):
        # Return the first planet in a list that intersects the line AB
        A, B = planets.index(planet1), planets.index(planet2)
        return any((sign(b - A, a - B) == sign(a, b)
                    for a in range(abs(a - B), root(a - B, b - A))
                    for b in range(abs(a - B), root(a - B, b - A))))

    return tuple(planet for planet in planets if check(planet1, planet2))

