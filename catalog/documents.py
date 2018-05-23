# this is created for elastic search indexing.
# elasticsearch installed on HP laptop:
# /c/Users/Dzmitry/elasticsearch-5.6.9/elasticsearch-5.6.9/bin
# to start elastic search: go to above directory and run: ./elasticsearch.bat
# to test elasticsearch server running: curl 'http://localhost:9200/?pretty'



from django_elasticsearch_dsl import DocType, Index
from catalog.models import Book

books = Index('books')

@books.doc_type
class booksDocument(DocType):
    class Meta:
        model = Book

        fields = [
            'title',
            'summary',
        ]