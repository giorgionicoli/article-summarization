class Prompt:
    text: str


class Summary:
    text: str
    model: str  # 'BART', 'T5', 'PEGASUS'...
    ranking: str  # '1st of 8'
    has_allucination: bool


class Judge:
    model: str
    prompt: Prompt
    score_type: str


class Focus:
    target: str
    type: str


class Evaluations:
    prompt: Prompt
    summaries: list[Summary]
    judge: Judge


class Entity:
    name: str
    type: str
    model: str


class Article:
    title: str
    text: str
    entities: list[Entity]


class Excerpt:
    text: str
    focus: list[Focus]
    evaluations: list[Evaluations]


class Sample:
    article: Article
    excerpts: list[Excerpt]


class DataSet:
    samples: list[Sample]
