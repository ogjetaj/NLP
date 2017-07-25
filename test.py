import cPickle as pickle

dataset = pickle.load( open( "dataset_100", "rb" ) )
correct_c1c2_dataset = []

for instance in dataset:
    correct = 0

    # First Filter
    # Instance in the correct format, nr of elements is the same for both
    instance_labels = instance.keys()
    #instance_values = instance.values()
    if len(instance_labels) == 8:
        # PASS
        # Second Filter
        # c1 and c2 in the correct format
        for item in instance:
            if item == 'c1' and instance[item].find('::bn') !=-1 :
                #print item, instance[item]
                correct +=1
            if item  == 'c2' and instance[item].find('::bn') != -1 :
                #print item, instance[item]
                correct +=1
    if correct == 2:
        correct_c1c2_dataset.append(instance)

#correct_c1c2_dataset
correct_context_dataset = []
for element in correct_c1c2_dataset:
    context = str()
    c1 = str()
    c2 = str()
    for item in element:
        if item == 'context':
            context = element[item]
        if item  == 'c1':
            word,babelnet = element[item].split('::')
            c1 = word
        if item == 'c2':
            word,babelnet = element[item].split('::')
            c2 = word
    if c1 in context and c2 in context:
        correct_context_dataset.append(element)

print len(correct_context_dataset)
