
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
    dict = {'Mercury':[0, 0.3958, 4.87], 'Venus':[0.723, 0.723, 6.24], 'Earth':[1, 1, 6.371], 'Mars':[1.52, 1.52, 3.71], 'Jupiter':[2, 2,  16.90], 'Saturn':[0.58, 0.58, 10.44], 'Uranus':[0.86, 0.86, 19.13]}
    r1, r2, v = dict[planet1], dict[planet2], []
    if planet1 not in dict or planet2 not in dict:
        return tuple()
    v.append(dict[planet1][2] / dict[planet1][1])
    v.append(dict[planet2][2] / dict[planet2][1])
    for i in range(2):
        if v[i] > 0:
            v[i] = (-1/v[i])**(1/2)
        v[i] = str(v[i])
    v = tuple(v)
    r1, r2 = r1[:2]/r1[2], r2[:2]/r2[2]
    for i in range(2):
        if r1 > r2 and v[i] > v[1-i]:
            v[1-i], v[i] = v[i], v[1-i]
        elif r1 < r2 and v[i] < v[1-i]:
            v[1-i], v[i] = v[i], v[1-i]
    for i in range(2):
        v[i] = int(v[i])
    v = (''.join(v))
    if r1 > r2:
        return (v,)
    else:
        return (v,) + bf(planet2, planet1)
