Number of Intersections among n chords
==========

Chords are described by (theta1, theta2), where theta1 is the lower angle of first end point and theta2 is the theta of other end point when points are represented in (r,theta) coordinate system. theta1 < theta2

Algorithm :

0. Sort all the chords with their low end points : theta(n*logn)
1. Label each low end point and high end point with the same number as index of chord number:  theta(n)
2. Sort the end points and form the final array of labels: theta(n*logn)
3. Make an augmented RBTree (balanced) in this way: (augmented with number of nodes in a tree rooted at a particular node i.e. order statistic tree)

count =0
for each label in sequence:

 count= count + modified_search(label)
 
where modified_search works like this: 
 - search for that label
 - if not found : insert it and change the information accordingly at other nodes; return 0
 - if found: delete it and count number of end points greater than that  label i.e. information at the node right of it ; return count

3 takes theta(n*logn) time.

I have written the code for 1 and 2. It is really time consuming to implement Order statistic RBTree in Python and I have less experience with such trees. I have been waiting for the response on stackoverflow for the solution to Python's RBTree library if it exists (http://stackoverflow.com/questions/26599741/order-statistic-red-black-binary-tree-in-python). 
