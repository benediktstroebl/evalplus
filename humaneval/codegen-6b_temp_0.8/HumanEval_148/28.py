
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
    if planet1=="Saturn" or planet2=="Saturn":
        return ()
    if planet1=="Venus" or planet2=="Venus":
        return ()
    if planet1=="Mars" or planet2=="Mars":
        return ()
    if planet1=="Jupiter" or planet2=="Jupiter":
        return ()
    if planet1=="Uranus" or planet2=="Uranus":
        return ()
    if planet1=="Neptune" or planet2=="Neptune":
        return ()
    if planet1=="Earth" or planet2=="Earth":
        return ()
    planet = {
        "Mercury": [0,0,1/4*math.pi,0],
        "Venus": [0,0,math.pi,0],
        "Earth": [0,0,2*math.pi,0],
        "Mars": [0,math.pi,3*math.pi/2,0],
        "Jupiter": [2*math.pi,0,5*math.pi/2,0],
        "Saturn": [0,math.pi,7*math.pi/2,0],
        "Uranus": [0,0,0,2*math.pi],
        "Neptune": [0,0,0,3*math.pi]
    }
    def sign(x):
        if x<0:
            return -1
        else:
            return 1
    def hyp(r1,r2,t1,t2):
        return math.sqrt((r1*r2)*(math.cos(t1-t2))**2)
    def f(planet1,planet2):
        r1, r2 = planet[planet1][0], planet[planet2][0]
        t1, t2 = planet[planet1][1], planet[planet2][1]
        k = planet[planet1][2]
        m = planet[planet2][2]
        hyp = hyp(r1,r2,t1,t2)
        s = sign(t2-t1)