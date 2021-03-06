from dataset import DatasetForDASH
from model import MultiNetwork
from option import opt
from tester import Tester
import template

model = MultiNetwork(template.get_nas_config(opt.quality))
dataset = DatasetForDASH(opt)
evaluator = Tester(opt, model, dataset)
evaluator.evaluate_quality()
#evaluator.evaluate_runtime()
