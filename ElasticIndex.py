from elasticsearch import Elasticsearch

class ElasticIndex:
	"""docstring for ElasticIndex"""

	def __init__(self, password, path_ca, index_name, server="https://localhost:9200/", user="elastic"):
		print("[*] Init elastic cluster")

		self.es = Elasticsearch(
		    server,
		    ca_certs=path_ca,
		    basic_auth=(user, password)
		)
		print("[**] Connected to the elastic cluster\n{}".format(self.es.info()))

		# Index variables
		self.index_name = index_name
		print("[**] Index name: {}".format(self.index_name))
		print("[**] Elastic Connected")

	def query(self, query):
		result = self.es.search(index=self.index_name, body=query)

		print("[*] Result query on {}".format(self.index_name))

		for hit in result['hits']['hits']:
		    print(hit['_source'])

	def send_data(self, data, verbose=False):
		for item in data:
			# print(item)

			response = self.es.index(index=self.index_name, body=item)

			if verbose:
				print(response)

		print("[*] Data added in index {}".format(self.index_name))

	def delete_all(self, verbose=False):
		# Define a query that matches all documents
		query = {
		    "query": {
		        "match_all": {}
		    }
		}

		response = self.es.delete_by_query(index=self.index_name, body=query)

		if verbose:
			print(response)



if __name__ == '__main__':	
	ei = ElasticIndex(
	 	password="XXXXXXXX",
		path_ca="../elasticsearch-8.15.1/config/certs/http_ca.crt",
		index_name="XXXXXXXX"
	)

	query = {
	    "query": {
	        "match_all": {}
	    }
	}

	# ei.query(query)
