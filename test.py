import os,sys
import json

pdtb_file = open('data/trial/pdtb_trial_data.json')

relations = [ json.loads(x) for x in pdtb_file ]
print len(relations)
example_relation = relations[10]

parse_file = open('data/trial/pdtb_trial_parses.json')
parse_dict = json.loads(parse_file.read())
doc_id = example_relation['DocID']
#the constituent parse
print parse_dict[doc_id]['sentences'][15]['parsetree']
#get the dependency parse
#(dependency type, HEAD token-token position, DEPENDENT token-token position)
print parse_dict[doc_id]['sentences'][15]['dependencies']
#get part of speech tags
print parse_dict[doc_id]['sentences'][15]['words'][0][1]['PartOfSpeech']
print parse_dict[doc_id]['sentences'][15]['words'][1]
