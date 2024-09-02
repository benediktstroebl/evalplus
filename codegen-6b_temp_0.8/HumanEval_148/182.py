
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
    planet_planet = P
    n = len(planet_planet)
    for i in xrange(n):
        for j in xrange(i+1,n):
            if planet_planet[j]['orbit'] > planet_planet[i]['orbit']:
                t = planet_planet[i]
                planet_planet[i] = planet_planet[j]
                planet_planet[j]= t
    s= []
    for planet1 in planet_planet:
        for planet2 in planet_planet:
            if planet1['orbit'] > planet2['orbit']:
                if planet1['orbit'] - planet2['orbit'] > 0:
                    s.append(planet2['name'])
    return tuple(s)

