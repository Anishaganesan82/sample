import pysolr

# Connect to the source SolrCloud instance
source_url = 'http://localhost:8983/solr/sample'
source_solr = pysolr.Solr(source_url)

# Connect to the target SolrCloud instance
target_url = 'http://localhost:8984/solr/new'
target_solr = pysolr.Solr(target_url)

# Query and iterate over the documents in the source collection
query = '*:*'
results = source_solr.search(query, rows=1000)
for doc in results:
    # Remove "_version_" field if present (not needed for indexing)
    if "_version_" in doc:
        del doc["_version_"]
    
    # Index each document to the target collection
    target_solr.add([doc])

# Commit the changes to the target collection
target_solr.commit()

print("Data transfer completed.")