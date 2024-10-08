
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

    orbital_dic = {"Mercury": 0.387, "Venus": 0.723, "Earth": 1, "Mars": 1.524, "Jupiter": 11.86, "Saturn": 29.44, "Uranus": 84.01, "Neptune": 164.79}
    a = orbital_dic[planet1]
    b = orbital_dic[planet2]
    list = []
    for i in orbital_dic:
        if orbital_dic[i] > a and orbital_dic[i] < b:
            list.append(i)
    return tuple(list)

