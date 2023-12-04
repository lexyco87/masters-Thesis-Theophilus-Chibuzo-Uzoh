import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='yolo7.pt',
                        help='initial weights path')
    parser.add_argument('--cfg', type=str, default='', help='model.yaml path')
    parser.add_argument('--data', type=str, default='iseauto_data/iseatuo.yaml',
                        help='data.yaml path')
    parser.add_argument('--hyp', type=str, default='data/hyp.scratch.p5.yaml',
                        help='hyperparameters path')
    parser.add_argument('--epochs', type=int, default=300)
    parser.add_argument('--batch-size', type=int, default=16,
                        help='total batch size for all GPUs')
    parser.add_argument('--img-size', nargs='+', type=int, default=[640, 640],
                        help='[train, test] image sizes')
    parser.add_argument('--rect', action='store_true',
                        help='rectangular training')
    parser.add_argument('--resume', nargs='?', const=True, default=False,
                        help='resume most recent training')
    parser.add_argument('--nosave', action='store_true',
                        help='only save final checkpoint')
    parser.add_argument('--notest', action='store_true',
                        help='only test final epoch')
    parser.add_argument('--noautoanchor', action='store_true',
                        help='disable autoanchor check')
    parser.add_argument('--evolve', action='store_true',
                        help='evolve hyperparameters')
    parser.add_argument('--bucket', type=str, default='', help='gsutil bucket')
    parser.add_argument('--cache-images', action='store_true',
                        help='cache images for faster training')
    parser.add_argument('--image-weights', action='store_true',
                        help='use weighted image selection for training')
    parser.add_argument('--device', default='',
                        help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--multi-scale', action='store_true',
                        help='vary img-size +/- 50%%')
    parser.add_argument('--single-cls', action='store_true',
                        help='train multi-class data as single-class')
    parser.add_argument('--adam', action='store_true',
                        help='use torch.optim.Adam() optimizer')
    parser.add_argument('--sync-bn', action='store_true',
                        help='use SyncBatchNorm, only available in DDP mode')
    parser.add_argument('--local_rank', type=int, default=-1,
                        help='DDP parameter, do not modify')
    parser.add_argument('--workers', type=int, default=8,
                        help='maximum number of dataloader workers')
    parser.add_argument('--project', default='runs/train',
                        help='save to project/name')
    parser.add_argument('--entity', default=None, help='W&B entity')
    parser.add_argument('--name', default='exp', help='save to project/name')
    parser.add_argument('--exist-ok', action='store_true',
                        help='existing project/name ok, do not increment')
    parser.add_argument('--quad', action='store_true', help='quad dataloader')
    parser.add_argument('--linear-lr', action='store_true', help='linear LR')
    parser.add_argument('--label-smoothing', type=float, default=0.0,
                        help='Label smoothing epsilon')
    parser.add_argument('--upload_dataset', action='store_true',
                        help='Upload dataset as W&B artifact table')
    parser.add_argument('--bbox_interval', type=int, default=-1,
                        help='Set bounding-box image logging interval for W&B')
    parser.add_argument('--save_period', type=int, default=-1,
                        help='Log model after every "save_period" epoch')
    parser.add_argument('--artifact_alias', type=str, default="latest",
                        help='version of dataset artifact to be used')
    parser.add_argument('--freeze', nargs='+', type=int, default=[0],
                        help='Freeze layers: backbone of yolov7=50, first3=0 1 2')
    parser.add_argument('--v5-metric', action='store_true',
                        help='assume maximum recall as 1.0 in AP calculation')
    opt = parser.parse_args()

    print(opt.data.endswith('coco.yaml'))
