import networkx as nx

"""General Estimator base class."""

class Estimator(object):
    """Estimator base class with constructor and public methods."""

    def __init__(self):
        """Creatinng an estimator."""
        pass

    def fit(self):
        """Fitting a model."""
        pass

    def get_embedding(self):
        """Getting the embeddings (graph or node level)."""
        return None

    def get_memberships(self):
        """Getting the membership dictionary."""
        return None

    def get_cluster_centers(self):
        """Getting the cluster centers."""
        return None

    def _check_connectivity(self, graph):
        """Checking the connected nature of a single graph."""
        try:
            connected = nx.is_connected(graph)
            if not connected:
                raise ValueError('Graph is not connected.')
        except:
            exit('Graph is not connected.')

    def _check_directedness(self, graph):
        """Checking the undirected nature of a single graph."""
        try:
            directed = nx.is_directed(graph)
            if directed:
                raise ValueError('Graph is not undirected.')
        except:
            exit('Graph is not undirected.')

    def _check_graph(self, graph):
        """We check the Karate Club assumptions about the graph."""
        self._check_connectivity(graph)
        self._check_directedness(graph)


    def _check_graphs(self, graphs):
        """We check the Karate Club assumptions for a list of graphs."""
        try:
            for graph in graphs:
                self._check_graph(graph)
        except:
            exit("The graph list do not satisfy requirements.")




 
        
        

