
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

    # Get the orbits of the planets
    orbit_1 = get_orbit(planet1)
    orbit_2 = get_orbit(planet2)
    
    # Get the difference in semimajor axis between the orbits
    distance = orbit_2.semi_major_axis - orbit_1.semi_major_axis
    
    # Get all the planets whose orbits are between the orbits of planet1 and planet2
    planets = get_orbit(planet1).semi_major_axis + 1.0E-6 * distance:
    for orbit in sorted(planets, key=lambda x: (x.semi_major_axis, x.mean_distance)):
        yield orbit
    
    # Return an empty tuple if there are no planets found
    if not any(planet._name for planet in planets):
        return tuple()
