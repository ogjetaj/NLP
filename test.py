import cPickle as pickle

dataset = pickle.load( open( "dataset_100", "rb" ) )
correct_c1c2_dataset = []

for instance in dataset:
    correct = 0
    # First Filter, Instance in the correct format, nr of elements is the same for both

    instance_labels = instance.keys()
    if len(instance_labels) == 8:
        # Second Filter, c1 and c2 in the correct format
        if instance['c1'].find('::bn') != -1:
            correct +=1
        if instance['c2'].find('::bn') != -1:
            correct +=1

    if correct == 2:
        correct_c1c2_dataset.append(instance)

# Third Filter, Context has c1 & c2

correct_context_dataset = []
for element in correct_c1c2_dataset:
    context = element['context']
    phrase_c1, babelnetID_c1 = element['c1'].split('::')
    phrase_c2, babelnetID_c2 = element['c2'].split('::')
    if phrase_c1 in context and phrase_c2 in context:
        correct_context_dataset.append(element)



for data in correct_c1c2_dataset:
    print data['context']


#print len(correct_context_dataset)
