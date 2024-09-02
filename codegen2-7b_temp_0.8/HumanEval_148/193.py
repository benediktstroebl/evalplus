
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
    if planet1 in Planets and planet2 in Planets:
        planets_distance = []
        if planet1 == "Earth" or planet2 == "Earth":
            planets_distance.append(planet1)
            planets_distance.append(planet2)
            return tuple(planets_distance)
        else:
            for planet in Planets:
                if planet.name == planet1 and planet.distance > planet.distance_to_sun:
                    planets_distance.append(planet)
                if planet.name == planet2 and planet.distance > planet.distance_to_sun:
                    planets_distance.append(planet)
            return tuple(planets_distance)
    else:
        return
