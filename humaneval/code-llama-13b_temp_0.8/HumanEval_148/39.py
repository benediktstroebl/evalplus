
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

    planets = {
        'Mercury': 0.4, 'Venus': 0.7, 'Earth': 1,
        'Mars': 1.5, 'Jupiter': 5.2, 'Saturn': 9.5,
        'Uranus': 19.2, 'Neptune': 30
    }
    if planet1 not in planets or planet2 not in planets:
        return ()
    planets = sorted(planets.items(), key = lambda x:x[1])
    planets = [planet[0] for planet in planets]
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    return tuple(planets[planet1_index+1: planet2_index])
