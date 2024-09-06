
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
    # your code here
    if (planet1 in solar_system) and (planet2 in solar_system):
        b = []
        for i in range(0, len(solar_system)):
            if (solar_system[i]!= planet1) and (solar_system[i]!= planet2):
                if (planet1_orbits[i] >= solar_system.index(planet1)) and (planet1_orbits[i] < solar_system.index(planet2)):
                    b.append(solar_system[i])
                elif (planet2_orbits[i] > solar_system.index(planet1)) and (planet2_orbits[i] <= solar_system.index(planet2)):
                    b.append(solar_system[i])
        b = tuple(b)
    else:
        b = ()
    return b
