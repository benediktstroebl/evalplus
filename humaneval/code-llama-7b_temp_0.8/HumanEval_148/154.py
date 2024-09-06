
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
    from planet_data import data
    # store data in dictionary
    all_planets = {
        "mercury" : data[0],
        "venus" : data[1],
        "earth" : data[2],
        "mars" : data[3],
        "jupiter" : data[4],
        "saturn" : data[5],
        "uranus" : data[6],
        "neptune" : data[7]
    }
    
    # check if the planet is in dictionary
    if planet1 not in all_planets or planet2 not in all_planets:
        return ()

    # get the data of the planets
    planet1_data = all_planets[planet1]
    planet2_data = all_planets[planet2]
    # get the orbit of the planets
    orbit1 = planet1_data[0]
    orbit2 = planet2_data[0]

    # get the list of planets
    planets = [planet1, planet2]
    # add the planets in between the orbit1 and orbit2
    for planet in all_planets:
        if all_planets[planet][0] > orbit1 and all_planets[planet][0] < orbit2:
            planets.append(planet)

    # sort planets by the closes to the sun
    return tuple(sorted(planets, key = lambda x: all_planets[x][0]))
