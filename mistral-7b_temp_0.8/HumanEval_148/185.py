
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

    import itertools
    import numpy as np
    planet_names = itertools.product('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    planet_distances = np.array([0, .723, 1, 1.524, 5.203, 9.539, 19.191, 30.068])
    planet_orbits = list(zip(planet_names, planet_distances))

    def validate(planet):
        return planet in planet_names

    def compute(planet1, planet2):
        if not all(validate(planet) for planet in [planet1, planet2]):
            return ()
        else:
            planet1_idx = planet_orbits.index([planet1, 0])
            planet2_idx = planet_orbits.index([planet2, 0])
            return planet_orbits[planet1_idx:planet2
