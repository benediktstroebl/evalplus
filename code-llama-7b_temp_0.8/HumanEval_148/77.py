
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
    planet_dict = {
        "mercury" : 0,
        "venus" : 1,
        "earth" : 2,
        "mars" : 3,
        "jupiter" : 4,
        "saturn" : 5,
        "uranus" : 6,
        "neptune" : 7
        }

    if planet1 in planet_dict and planet2 in planet_dict:
        if planet_dict[planet1] < planet_dict[planet2]:
            min_planet, max_planet = planet1, planet2
        else:
            min_planet, max_planet = planet2, planet1

        min_planet_number = planet_dict[min_planet]
        max_planet_number = planet_dict[max_planet]
        return tuple(planet_dict.keys()[planet_dict.values().index(i)] 
                    for i in range(min_planet_number + 1, max_planet_number))
    else:
        return ()
