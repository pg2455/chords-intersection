# define lower end_point as an object
class lower():

    def __init__(self, lower,label):
        self.lower = lower
        self.label = label

    def value(self):
        return self.lower

    def lab(self):
        return self.label
        
# define upper end _point as an object
class upper():

    def __init__(self, upper, label):
        self.upper =  upper
        self.label = label

    def value(self):
        return self.upper

    def lab(self):
        return self.label
# define chord as an object
class chord(lower, upper):

    def __init__(self, theta_l, theta_u, label):
        self.lower = lower(theta_l, label)
        self.upper = upper(theta_u, label)
        self.label = label

    def l(self):
        return self.lower.value()

    def u(self):
        return self.upper.value()

    def interval(self):
        return self.lower, self.upper

    def lab(self):
        return self.label

###################################################
data = [(1,3),(1.5,5),(2,7),(3,4)] # data format
data = sorted(data, key = lambda (x,y): x)
chords =[chord(l,u,x) for x,(l,u) in enumerate(data)] # store data in chord format
points = [end_point for each in chords for end_point in each.interval()] # convert intervals to point format

# theta(nlogn)
final = sorted(points, key=lambda point : point.value()) # sort as per end_points; since all these are objects, labels will be preserved
values = [i.value() for i in final] # get values
labels = [i.lab() for i in final] # get final labels to build BST
####################################################
