test = {
  'name': 'Question 9_a_median_vs_mean',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'a_median_vs_mean'
          >>> 'a_median_vs_mean' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'a_median_vs_mean'
          >>> # from its initial state (of ...)
          >>> a_median_vs_mean is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(a_median_vs_mean, -70.4214)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
