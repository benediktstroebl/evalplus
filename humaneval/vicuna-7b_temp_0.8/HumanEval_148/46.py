
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
    # get the distances to the sun for each planet
    distances = {planet: get_distance(planet, 'sun') for planet in planet1, planet2}
    # get the orbits of the planets
    orbits = {planet: get_orbit(planet) for planet in planet1, planet2}
    # create a list of all the planets whose orbit is between the orbits of the two given planets
    filtered_planets = [planet for planet in orbits if get_orbit(planet) not in (orbit1, orbit2) and get_distance(planet, 'sun') > distances[planet]]
    # sort the list by proximity to the sun
    filtered_planets.sort(key=lambda planet: abs(get_distance(planet, 'sun')))
    # return the filtered planets
    return filtered_planets
