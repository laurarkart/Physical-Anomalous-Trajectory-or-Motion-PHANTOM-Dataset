import json

classes = {
	'Pushing something so that it falls off the table': 'pen',
	'Something falling like a feather or paper': 'paper',
	'Rolling something on a flat surface': 'pen',
	'Showing that something is empty': 'cup',
	'Putting something on a surface': 'pen',
	'Tearing something into two pieces': 'paper',
	'Unfolding something': 'paper',
	'Taking one of many similar things on the table': 'pen',
	'Closing something': 'box',
	'Plugging something into something': 'cable'
}


def get_ids():

	train_ids = {}
	test_ids = {}
	for class_name in classes:
		train_ids[class_name] = list()
		test_ids[class_name] = list()

	with open('something-something-v2-train.json') as json_file:
		train_data = json.load(json_file)

	with open('something-something-v2-validation.json') as json_file:
		test_data = json.load(json_file)

	for data in [train_data, test_data]:
		for vid_data in data:
			class_name = vid_data['template'].replace('[', '').replace(']', '')
			placeholder = vid_data['placeholders'][0]

			if class_name in classes:

				for class_label, sub_item in classes.items():
					if class_name == class_label and sub_item in placeholder:
						if data == train_data:
							train_ids[class_name].append(vid_data['id'])
						else:
							test_ids[class_name].append(vid_data['id'])

	return train_ids, test_ids


if __name__ == "__main__":
	train_labels, test_labels = get_ids()
