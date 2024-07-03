import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from segmentar_img import segmentar_imagem
#lista experimentos

lista_experimentos = [
     {
        'num_points': 256,
        'image': 'circulo.png',
        'max_points': 10
    },
    {
        'num_points': 256,
        'image': 'borboleta_simples.png',
        'max_points': 100
    },
   
    {
        'num_points': 256,
        'image': 'coracao.png',
        'max_points': 100
    },
]

# distancia euclidiana dos pontos
def distancia_euclidiana(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def voronoi(experimento, points=False):
    num_points = experimento['num_points']

    if points:
        points = np.random.rand(num_points, 2) * 100
    else:
        points = np.array(segmentar_imagem(experimento['image'], experimento['max_points']))
   
    # grid de pontos
    grid_size = num_points
    x = np.linspace(0, num_points, grid_size)
    y = np.linspace(0, num_points, grid_size)
    xv, yv = np.meshgrid(x, y)

    clrs = sns.color_palette('husl', n_colors=num_points)  # a list of RGB tuples
    fig, ax = plt.subplots(figsize=(5, 5))

    # Formando lista para o diagrama de voronoi
    voronoi_diagram = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            # setando um minimo com numero maximo para iniciar
            min_dist = float('inf')
            for k, point in enumerate(points):
                dist = distancia_euclidiana(point, (xv[i, j], yv[i, j]))
                if dist < min_dist:
                    min_dist = dist
                    voronoi_diagram[i, j] = k
    # definindo paleta de cores
    colormap = plt.cm.nipy_spectral
    ax.set_prop_cycle('color',[colormap(i) for i in np.linspace(0, 1,num_points)])

    plt.imshow(voronoi_diagram, extent=(0, num_points, 0, num_points), origin='lower', cmap=colormap, alpha=0.5)
    plt.scatter(points[:, 0], points[:, 1], color='red', edgecolors="black", s=100)
    plt.xlim(0, num_points)
    plt.ylim(0, num_points)
    plt.title('Voronoi Diagram')


voronoi({
    'num_points': 100,
}, True)
# for experimento in lista_experimentos:
#     voronoi(experimento)

plt.show()
