
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
    all_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in all_planets or planet2 not in all_planets:
        return ()
    elif planet1 == planet2:
        return (planet1,)
    else:
        final_list = []
        for i in range(len(all_planets)):
            if all_planets[i] == planet1:
                index1 = i
            elif all_planets[i] == planet2:
                index2 = i
        if index1 > index2:
            for i in range(index1 + 1, index2 + 1):
                final_list.append(all_planets[i])
        elif index1 < index2:
            for i in range(index1, index2 + 1):
                final_list.append(all_planets[i])
        final_list.sort()
        return tuple(final_list)

