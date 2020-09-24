import imageio
import os
import click


@click.command()
@click.argument('dir_name')
@click.argument('output_fname', default='temp')
def img_to_gif(dir_name, output_fname):
    imgs = []
    for fname in os.listdir(dir_name):
        imgs.append(imageio.imread(os.path.join(dir_name, fname)))
    imageio.mimsave(output_fname + '.gif', imgs)


if __name__ == "__main__":
    img_to_gif()
