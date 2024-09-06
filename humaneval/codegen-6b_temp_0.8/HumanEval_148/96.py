
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
    proximity_to_sun = lambda planet: abs(planet[0] - planet[1])
    orbital_radius = lambda planet: (6.0 * 10**-12) / (3.149 * 10**8)
    orbital_period = lambda planet: orbital_radius(planet) * 100000000
    planets = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0))
    # planets = ((0, 0), (1, 4.1 * 10**-15), (2, 6.4 * 10**-23), (3, 1.0 * 10**-10), (4, 2.8 * 10**-27), (5, 7.4 * 10**-40), (6, 1.0 * 10**-39), (7, 1.0 * 10**-27))
    planets = sorted(planets, key=proximity_to_sun)
    planets = sorted(planets, key=orbital_radius)
    planets = sorted(planets, key=orbital_period)
    planets = sorted(planets, key=lambda planet: planet[1])
    planets = sorted(planets, key=lambda planet: planet[0])
    planets = [planet for planet in planets if planet[0] > planet1 and planet[0] < planet2]
    return tuple(planets)
