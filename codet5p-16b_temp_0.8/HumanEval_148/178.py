
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
    'Mercury': (4, 5),
    'Venus': (9, 10),
    'Earth': (12, 13),
    'Mars': (6, 7),
    'Jupiter': (1, 11),
    'Saturn': (8, 15),
    'Uranus': (16, 17),
    'Neptune': (18, 19)
    }
    
    planet1 = planet1.lower()
    planet2 = planet2.lower()

    for planet in planets:
        if planet1 == planet or planet2 == planet:
            return tuple(sorted([planet for planet in planets if planet1 <= planet <= planet2], key=lambda planet: abs(planets[planet][0]-planets[planet1][0])+abs(planets[planet][1]-planets[planet1][1])))
    
    return tuple()
    
