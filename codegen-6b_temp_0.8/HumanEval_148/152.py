
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
    planets = {
             'Sun':(0,0,0,0,0,0,0),
             'Mercury':(0.39,0.60,1.83,0.20,0.49,1.06,0.10),
             'Venus':(0.70,1.10,0.24,0.61,0.25,0.72,0.25),
             'Earth':(1.00,0.52,0.65,1.10,0.99,1.06,0.97),
             'Mars':(1.66,1.62,0.42,2.36,1.49,0.76,0.66),
             'Jupiter':(5.21,5.79,6.05,3.72,5.68,5.99,5.68),
             'Saturn':(9.54,9.62,8.68,8.93,9.29,9.87,9.29),
             'Uranus':(19.19,19.54,19.21,19.61,19.78,19.87,19.78),
             'Neptune':(29.64,29.31,29.11,29.64,29.79,29.54,29.22)
    }
    line1 = planets[planet1]
    line2 = planets[planet2]

    sun = planets['Sun']
    x1 = 0
    x2 = 0
    line = []

    if planet1 == planet2 or planet2 not in planets:
        return tuple(line)

    while x1 < len(line1) and x2 < len(line2):
        for i in range(7):
            if line1[x1] <= sun[i] <= line2[x2]:
                line.append(line1[x1])
                x1 += 1
                break
            elif sun[i] < line1[x1]:
                x1 += 1
            elif line2[x2] < sun[i]:
                x2 += 1
            else:
                x1 += 1
                x2 += 1

    return tuple(line)
