
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
    #planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_orbit = {'Mercury': 0, 'Venus': 1, 'Earth': 2, 'Mars': 3, 'Jupiter': 4, 'Saturn': 5, 'Uranus': 6, 'Neptune': 7}

    if planet1 not in planet_names or planet2 not in planet_names:
        return tuple()

    orbit1 = planet_orbit[planet1]
    orbit2 = planet_orbit[planet2]
    planets = list()
    for planet in planet_names:
        orbit = planet_orbit[planet]
        if orbit > orbit1 and orbit < orbit2:
            planets.append(planet)
    planets.sort(key=lambda p: planet_orbit[p])
    return tuple(planets)
