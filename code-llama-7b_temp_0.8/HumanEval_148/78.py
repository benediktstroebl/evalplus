
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
    planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planets_num = [0, 1, 2, 3, 4, 5, 6, 7]
    if planet1 not in planet or planet2 not in planet:
        return ()
    else:
        if planet1 == planet2:
            return ()
        else:
            if planets_num[planet.index(planet1)] < planets_num[planet.index(planet2)]:
                index_1 = planets_num[planet.index(planet1)]
                index_2 = planets_num[planet.index(planet2)]
            else:
                index_1 = planets_num[planet.index(planet2)]
                index_2 = planets_num[planet.index(planet1)]
            index = index_1 + 1
            res = []
            while index < index_2:
                res.append(planet[index])
                index += 1
        return tuple(res)
    
    
