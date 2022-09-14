#This code is adopted from
#https://github.com/ming024/FastSpeech2
import argparse

from omegaconf import OmegaConf as OC

from preprocessor import paimon_22050


def main(args):
    hparams = OC.load(args.config)
    if "paimon_22050" in hparams.dataset:
        paimon_22050.prepare_align(hparams)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    main(args)
